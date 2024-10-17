Name:		texlive-cooperhewitt
Version:	64967
Release:	2
Summary:	LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for the Cooper Hewitt family of sans serif fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cooperhewitt
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooperhewitt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooperhewitt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Cooper Hewitt is a contemporary sans serif, with characters
composed of modified-geometric curves and arches. Initially
commissioned by Pentagram to evolve his Polaris Condensed
typeface, Chester Jenkins created a new digital form to support
the newly transformed Smithsonian Design Museum.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cooperhewitt
%{_texmfdistdir}/fonts/vf/public/cooperhewitt
%{_texmfdistdir}/fonts/type1/public/cooperhewitt
%{_texmfdistdir}/fonts/tfm/public/cooperhewitt
%{_texmfdistdir}/fonts/opentype/public/cooperhewitt
%{_texmfdistdir}/fonts/map/dvips/cooperhewitt
%{_texmfdistdir}/fonts/enc/dvips/cooperhewitt
%doc %{_texmfdistdir}/doc/fonts/cooperhewitt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
