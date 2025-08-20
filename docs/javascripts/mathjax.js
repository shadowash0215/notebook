window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true,
      macros: {
        abs: ["\\lvert #1 \\rvert", 1],
        op: ["\\operatorname{#1}", 1],
        ket: ["\\lvert #1 \\rangle", 1],
        bra: ["\\langle #1 \\rvert", 1],
        norm: ["\\lVert #1 \\rVert", 1],
        innerprod: ["\\langle #1, #2 \\rangle", 2],
        PRF: "\\mathsf{PRF}",
        Adv: "\\mathsf{Adv}",
        sk: "\\mathsf{sk}",
        pk: "\\mathsf{pk}",
        from: "\\leftarrow",
        poly: "\\mathsf{poly}",
        Pr: ["\\operatorname{Pr}[#1]", 1]
      }
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };
  
  document$.subscribe(() => { 
    MathJax.typesetPromise()
  })