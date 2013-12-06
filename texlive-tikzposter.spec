# revision 29942
# category Package
# catalog-ctan /graphics/pgf/contrib/tikzposter
# catalog-date 2013-04-04 11:28:51 +0200
# catalog-license lppl1.2
# catalog-version 1.1
Name:		texlive-tikzposter
Version:	1.1
Release:	5
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
%{_texmfdistdir}/tex/latex/tikzposter/tikzposter-colorthemes.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposter-layoutstyles.tex
%{_texmfdistdir}/tex/latex/tikzposter/tikzposter.cls
%doc %{_texmfdistdir}/doc/latex/tikzposter/README
%doc %{_texmfdistdir}/doc/latex/tikzposter/logo.png
%doc %{_texmfdistdir}/doc/latex/tikzposter/logoL.png
%doc %{_texmfdistdir}/doc/latex/tikzposter/logoR.png
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
