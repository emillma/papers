\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{iopconfser}[2022/11/30 IOP Conference Series LaTeX template]

\LoadClass[a4paper]{article}


% Margin settings from jpconf11.clo
\setlength{\hoffset}{0mm}
\setlength{\marginparsep}{0mm}
\setlength{\marginparwidth}{0mm}
\setlength{\textwidth}{160mm}
\setlength{\oddsidemargin}{-0.4mm}
\setlength{\evensidemargin}{-0.4mm}
\setlength{\voffset}{0mm}
\setlength{\headheight}{8mm}
\setlength{\headsep}{5mm}
\setlength{\footskip}{0mm}
\setlength{\textheight}{230mm}
\setlength{\topmargin}{1.6mm}

% More length definitions from jpconf11.clo
\setlength\maxdepth{.5\topskip}
\setlength\@maxdepth\maxdepth
\setlength\footnotesep{8.4\p@}
\setlength{\skip\footins} {10.8\p@ \@plus 4\p@ \@minus 2\p@}
\setlength\floatsep       {14\p@ \@plus 2\p@ \@minus 4\p@}
\setlength\textfloatsep   {24\p@ \@plus 2\p@ \@minus 4\p@}
\setlength\intextsep      {16\p@ \@plus 4\p@ \@minus 4\p@}
\setlength\dblfloatsep    {16\p@ \@plus 2\p@ \@minus 4\p@}
\setlength\dbltextfloatsep{24\p@ \@plus 2\p@ \@minus 4\p@}
\setlength\@fptop{0\p@}
\setlength\@fpsep{10\p@ \@plus 1fil}
\setlength\@fpbot{0\p@}
\setlength\@dblfptop{0\p@}
\setlength\@dblfpsep{10\p@ \@plus 1fil}
\setlength\@dblfpbot{0\p@}
\setlength\partopsep{3\p@ \@plus 2\p@ \@minus 2\p@}

% Clear the header and footer

\pagestyle{empty}

\renewcommand{\title}[1]{\vspace*{0mm}{\exhyphenpenalty=10000\hyphenpenalty=10000
        \fontsize{18bp}{24bp}\selectfont\bf\noindent\raggedright
        \textsf{#1}\par}}


\renewcommand{\author}[1]{\vspace*{1.5pc}%
    \fontsize{14bp}{16bp}\raggedright
    \begin{quote}\textbf{\textsf{#1}}\end{quote}}

\newcommand{\affil}[1]{\fontsize{10bp}{11bp}\selectfont\raggedright
    \begin{quote}#1\end{quote}
    \vspace*{-22pt}}

\newcommand{\email}[1]{\vspace*{12pt}\fontsize{10bp}{11bp}\selectfont\raggedright
    \begin{quote}E-mail: #1\end{quote}
    \vspace*{-22pt}}

\renewenvironment{abstract}{%
    \vspace{16pt plus3pt minus3pt}
    \begin{quote}
        \bfseries \abstractname.\quad\rm\ignorespaces} 
        {\end{quote}\vspace{5mm}}

% Section titles

\renewcommand\section{\@startsection {section}{1}{\z@}%
  {-3.25ex\@plus -1ex \@minus -.2ex}%
  {1sp}%
  {\reset@font\normalsize\bfseries\raggedright}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
    {-3.25ex\@plus -1ex \@minus -.2ex}%
    {1sp}%
    {\reset@font\normalsize\itshape\raggedright}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
    {-3.25ex\@plus -1ex \@minus -.2ex}%
    {-1em \@plus .2em}%
    {\reset@font\normalsize\itshape}}
\renewcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
    {3.25ex \@plus1ex \@minus.2ex}%
    {-1em}%
    {\reset@font\normalsize\itshape}}
\renewcommand\subparagraph{\@startsection{subparagraph}{5}{\parindent}%
    {3.25ex \@plus1ex \@minus .2ex}%
    {-1em}%
    {\reset@font\normalsize\itshape}}

\RequirePackage{csquotes}                   % recommended for biblatex
\RequirePackage{nicefrac}                   % recommended for biblatex
\RequirePackage[
    backend=biber,
    style=ieee,
    maxbibnames=99,
    minbibnames=3,
    maxcitenames=2,
    mincitenames=1,
    citestyle=numeric-comp,
    sorting=none,
    dashed=false
]{biblatex}                                 % for bibliography


\RequirePackage{xspace}
