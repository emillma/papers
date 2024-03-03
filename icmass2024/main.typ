#import "./template.typ": *

#import "./mypackages/acronyms.typ": make-glossary, print-glossary, gls, glspl 

#show: make-glossary
// #include "./glossary.typ"

#show: ieee.with(
  title: "A sensor Rig for Multi-Sensor Data Collection in Maritime",
  abstract: [
    #include "./parts/apbstract.typ"
  ],
  authors: (
    (
      name: "Emil Martens",
      department: [Dept of Engeneering Cybernetics],
      organization: [SFI Autoship],
      // location: [Trondheim, Norway],
      email: "emil.martens@ntnu.no"
    ),
    (
      name: "Annette Stahl",
      department: [Dept of Engeneering Cybernetics],
      // organization: [Affiliation],
      // location: [City, Country],
      email: "annette.stahl@ntnu.no"
    ),
  ),

  index-terms: ("Situation awareness", "Data collection", "Polarization cameras"),
  bibliography-file: "refs.bib",
)


= Acronyms
#print-glossary((
// minimal term
(key: "asv", short: "ASV", long: "Autonomous Surface Vehicle"),
// a term with a long form
(key: "unamur", short: "UNamur", long: "Université de Namur"),
// no long form here
(key: "kdecom", short: "KDE Community", desc:"An international team developing and distributing Open Source software."),
// a full term with description containing markup
(
  key: "oidc", 
  short: "OIDC", 
  long: "OpenID Connect", 
  desc: [OpenID is an open standard and decentralized authentication protocol promoted by the non-profit
    #link("https://en.wikipedia.org/wiki/OpenID#OpenID_Foundation")[OpenID Foundation].]),
),disable-back-references: true)