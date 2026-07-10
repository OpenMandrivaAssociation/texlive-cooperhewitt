%global tl_name cooperhewitt
%global tl_revision 78931

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the Cooper Hewitt family of...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cooperhewitt
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cooperhewitt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cooperhewitt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Cooper Hewitt is a contemporary sans serif, with characters composed of
modified-geometric curves and arches. Initially commissioned by
Pentagram to evolve his Polaris Condensed typeface, Chester Jenkins
created a new digital form to support the newly transformed Smithsonian
Design Museum.

