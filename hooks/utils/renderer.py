import os
import re
from hashlib import sha256

from mkdocs.utils import log

def _make_svg_ids_unique(svg_str: str, file_hash: str) -> str:
    # Make all ids in the svg unique by appending the file hash
    def replace_id(match: re.Match) -> str:
        return f'id="{match.group("id")}_{file_hash}"'

    svg_str = re.sub(r'id=\'(?P<id>[^\']+)\'', replace_id, svg_str)

    def replace_ref(match: re.Match) -> str:
        return f'xlink:href=\'#{match.group("id")}_{file_hash}\''
    
    svg_str = re.sub(r'xlink:href=\'#(?P<id>[^\']+)\'', replace_ref, svg_str)

    return svg_str

class TeXError(BaseException):
    pass


class TeXWriterConfig:
    def __init__(self) -> None:
        self.compiler = "xelatex"
        self.preamble = ""


class TeXWriter:
    def __init__(self, config=TeXWriterConfig()) -> None:
        self.config = config

    def create_tex_file(self, content: str, tex_name: str) -> None:
        """
        Write content into tex_name, with preamble set by config
        """
        full_tex = (
            "\n\n".join(
                (self.config.preamble, "\\begin{document}", content, "\\end{document}")
            )
            + "\n"
        )

        try:
            with open(f"{tex_name}.tex", "w", encoding="utf-8") as tex_file:
                tex_file.write(full_tex)
        except OSError:
            log.error("[qcircuit] unable to create tex file!")

    def create_svg_from_tex(self, tex_name: str) -> None:
        """
        Generate svg from tex file
        """
        if self.config.compiler == "xelatex":
            program = "xelatex -no-pdf"
        else:
            raise NotImplementedError(
                f"Compiler {self.config.compiler} is not implemented!"
            )

        log.info(f"rendering {tex_name}.svg")

        # use compiler to transform tex to pdf
        tex2xdv_cmd = " ".join(
            (
                program,
                "-halt-on-error",
                "-interaction=batchmode",
                f'"{tex_name}.tex"',
                ">",
                os.devnull,
            )
        )
        log.debug(f"running {tex2xdv_cmd}")
        if os.system(tex2xdv_cmd):
            log.error("LaTeX Error! Not a worry, it happens to the best of us.")
            raise TeXError("LaTeX Error! Look into log file for detail")

        # use dvisvgm to transform xdv to svg
        xdv2svg_cmd = " ".join(
            (
                "dvisvgm",
                f'"{tex_name}.xdv"',
                "-n",
                "-v 0",
                f'-o "{tex_name}.svg"',
                ">",
                os.devnull,
            )
        )
        log.debug(f"running {xdv2svg_cmd}")
        if os.system(xdv2svg_cmd):
            log.error("dvisvgm Error!")
            raise TeXError("dvisvgm Error!")

        # clean up
        for ext in (".log", ".aux", ".xdv", ".tex"):
            try:
                os.remove(tex_name + ext)
            except FileNotFoundError:
                pass

class TikZAutomataRenderer:
    def __init__(self, options: str, contents: str) -> None:
        self.options = options
        self.contents = contents

    def write_to_svg(self, cachefile: bool) -> str:
        filename = sha256(
            self.contents.encode() + (self.options.encode() if self.options else b"")
        ).hexdigest()

        if cachefile:
            try:
                os.chdir("cache/automata")
            except OSError:
                log.error("[tikzautomata] cache directory not found!")

        if cachefile and os.path.exists(f"{filename}.svg"):
            log.debug("[tikzautomata] load from existing file...")
            with open(f"{filename}.svg", "r", encoding="utf-8") as f:
                svg_str = f.read(None)
            os.chdir("../..")
            return svg_str

        writer = TeXWriter()
        writer.config.preamble = r'''
\documentclass[dvisvgm]{standalone}
\usepackage{tikz}
\usepackage{amsmath}
\usepackage{amssymb}

\usetikzlibrary {arrows.meta,automata,positioning,shapes.geometric}
        '''
        begin_command = r"\begin{tikzpicture}[%s]" % self.options if self.options else r"\begin{tikzpicture}[->,>={Stealth[round]},shorten >=1pt,auto,node distance=2cm,on grid,semithick,inner sep=2pt,bend angle=50,initial text=]"
        writer.create_tex_file("\n".join((
            begin_command,
            self.contents.strip(),
            r'''\end{tikzpicture} 
'''
        )), filename)

        writer.create_svg_from_tex(filename)

        with open(f"{filename}.svg", "r", encoding="utf-8") as f:
            svg_str = f.read(None)

        svg_str = _make_svg_ids_unique(svg_str, filename)

        # clean up
        if cachefile == True:
            with open(f"{filename}.svg", "w", encoding="utf-8") as f:
                f.write(svg_str)
        else: 
            try:
                os.remove(filename + ".svg")
            except FileNotFoundError:
                pass

        os.chdir("../..")

        return svg_str
    
class MathenvRenderer:
    def __init__(self, options: str, contents: str) -> None:
        self.options = options
        self.contents = contents

    def write_to_svg(self, cachefile: bool) -> str:
        filename = sha256(
            self.contents.encode() + (self.options.encode() if self.options else b"")
        ).hexdigest()

        if cachefile:
            try:
                os.chdir("cache/mathenv")
            except OSError:
                log.error("[mathenv] cache directory not found!")

        if cachefile and os.path.exists(f"{filename}.svg"):
            log.debug("[mathenv] load from existing file...")
            with open(f"{filename}.svg", "r", encoding="utf-8") as f:
                svg_str = f.read(None)
            os.chdir("../..")
            return svg_str

        writer = TeXWriter()
        writer.config.preamble = r'''
\documentclass[dvisvgm]{standalone}
\usepackage{tikz}
\usepackage{amssymb}
\usepackage{amsmath}
\usetikzlibrary{cd}
\usetikzlibrary{decorations.markings}
\tikzset{double line with arrow/.style args={#1,#2}{decorate,decoration={markings,%
mark=at position 0 with {\coordinate (ta-base-1) at (0,1pt);
\coordinate (ta-base-2) at (0,-1pt);},
mark=at position 1 with {\draw[#1] (ta-base-1) -- (0,1pt);
\draw[#2] (ta-base-2) -- (0,-1pt);
}}}}
        '''
        begin_command = r"\begin{tikzcd}[%s]" % self.options if self.options else r"\begin{tikzcd}"
        writer.create_tex_file("\n".join((
            begin_command,
            self.contents.strip(),
            r'''\end{tikzcd} 
'''
        )), filename)

        writer.create_svg_from_tex(filename)

        with open(f"{filename}.svg", "r", encoding="utf-8") as f:
            svg_str = f.read(None)

        svg_str = _make_svg_ids_unique(svg_str, filename)

        # clean up
        if cachefile == True:
            with open(f"{filename}.svg", "w", encoding="utf-8") as f:
                f.write(svg_str)
        else: 
            try:
                os.remove(filename + ".svg")
            except FileNotFoundError:
                pass

        os.chdir("../..")

        return svg_str


class QcircuitRenderer:
    def __init__(self, options: str, contents: str) -> None:
        self.options = options
        self.contents = contents

    def write_to_svg(self, cachefile: bool) -> str:
        filename = sha256(self.contents.encode()).hexdigest()

        if cachefile == True:
            try:
                os.chdir("cache/qcircuit")
            except OSError:
                log.error("[Qcircuit] cache directory not found!")

        if cachefile == True and os.path.exists(f"{filename}.svg"):
            log.debug("[Qcircuit] load from existing file...")
            with open(f"{filename}.svg", "r", encoding="utf-8") as f:
                svg_str = f.read(None)
            os.chdir("../..")
            return svg_str

        writer = TeXWriter()
        writer.config.preamble = r'''
\documentclass[dvisvgm]{standalone}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[braket]{qcircuit}

        '''
        begin_command = r"\Qcircuit %s {" % self.options if self.options else r"\Qcircuit @C=1.0em @R=2.0em {"
        writer.create_tex_file("\n".join((
            begin_command,
            self.contents.strip(),
            r'''} 
'''
        )), filename)

        writer.create_svg_from_tex(filename)

        with open(f"{filename}.svg", "r", encoding="utf-8") as f:
            svg_str = f.read(None)

        svg_str = _make_svg_ids_unique(svg_str, filename)

        # clean up
        if cachefile == True:
            with open(f"{filename}.svg", "w", encoding="utf-8") as f:
                f.write(svg_str)
        else: 
            try:
                os.remove(filename + ".svg")
            except FileNotFoundError:
                pass

        os.chdir("../..")

        return svg_str

class AlgorithmRenderer:
    def __init__(self, options: str, contents: str) -> None:
        self.options = options
        self.contents = contents

    def write_to_svg(self, cachefile: bool) -> str:
        filename = sha256(self.contents.encode()).hexdigest()

        if cachefile == True:
            try:
                os.chdir("cache/algorithm")
            except OSError:
                log.error("[Algorithm] cache directory not found!")

        if cachefile == True and os.path.exists(f"{filename}.svg"):
            log.debug("[Algorithm] load from existing file...")
            with open(f"{filename}.svg", "r", encoding="utf-8") as f:
                svg_str = f.read(None)
            os.chdir("../..")
            return svg_str

        writer = TeXWriter()
        writer.config.preamble = r'''
\documentclass[dvisvgm]{standalone}
\usepackage{ctex}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[braket]{qcircuit}
\usepackage[ruled,linesnumbered]{algorithm2e}
\SetKwInput{KwData}{Runtime}
\SetKwInput{KwResult}{Procedure}
\renewcommand{\algorithmcfname}{Algorithm}
        '''
        begin_command = r"\begin{algorithm}[H] %s" % self.options if self.options else r"\begin{algorithm}[H]"
        writer.create_tex_file("\n".join((
            begin_command,
            self.contents.strip(),
            r'''\end{algorithm}
'''
        )), filename)

        writer.create_svg_from_tex(filename)

        with open(f"{filename}.svg", "r", encoding="utf-8") as f:
            svg_str = f.read(None)

        svg_str = _make_svg_ids_unique(svg_str, filename)

        # clean up
        if cachefile == True:
            with open(f"{filename}.svg", "w", encoding="utf-8") as f:
                f.write(svg_str)
        else: 
            try:
                os.remove(filename + ".svg")
            except FileNotFoundError:
                pass

        os.chdir("../..")

        return svg_str