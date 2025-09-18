window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true,
      macros: {
        op: ['\\operatorname{#1}', 1],
        from: '\\leftarrow',
        abs: ['\\left\\lvert#1\\right\\rvert', 1],
        norm: ['\\left\\lVert#1\\right\\rVert', 1],
        Pr: ['\\operatorname{Pr}\[#1\]', 1],
        innerproduct: ['\\left\\langle#1 \\vert #2\\right\\rangle', 2],
        ket: ['\\left\\lvert#1\\right\\rangle', 1],
        bra: ['\\left\\langle#1\\right\\rvert', 1],
        poly: ['\\operatorname{poly}\(#1\)', 1],
        PRF: '\\mathsf{PRF}',
        Adv: '\\operatorname{Adv}',
        sk: '\\mathsf{sk}',
        pk: '\\mathsf{pk}',
        i: '\\mathrm{i}',
        xRightarrow: ["\\stackrel{#1}{\\Rightarrow}", 1],
        xLeftarrow: ["\\stackrel{#1}{\\Leftarrow}", 1],
        dbrack: ['[\\![#1]\\!]', 1],
      }
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };
  
  document$.subscribe(() => { 
    MathJax.startup.output.clearCache()
    MathJax.typesetClear()
    MathJax.texReset()
    MathJax.typesetPromise()
  })