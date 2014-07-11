# revision 32732
# category Package
# catalog-ctan /graphics/pgf/contrib/tikzposter
# catalog-date 2014-01-20 12:50:28 +0100
# catalog-license lppl1.2
# catalog-version 2.0
Name:		texlive-tikzposter
Version:	2.0
Release:	3
Summary:	Create scientific posters using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzposter
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzposter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzposter.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzposter.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A document class provides a simple way of using TikZ for
generating posters. Several formatting options are available,
and spacing and layout of the poster is to a large extent
automated.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikzposter/tikzposter.cls
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterBackgroundstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterBlockstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterColorpalettes.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterColorstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterInnerblockstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterLayoutthemes.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterNotestyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposterTitlestyles.tex
%doc %{_texmfdistdir}/doc/latex/tikzposter/README
%doc %{_texmfdistdir}/doc/latex/tikzposter/tikzposter-example.tex
%doc %{_texmfdistdir}/doc/latex/tikzposter/tikzposter-template.tex
%doc %{_texmfdistdir}/doc/latex/tikzposter/tikzposter.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tikzposter/tikzposter.dtx
%doc %{_texmfdistdir}/source/latex/tikzposter/tikzposter.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
