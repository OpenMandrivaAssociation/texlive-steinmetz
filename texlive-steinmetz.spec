Name:		texlive-steinmetz
Version:	15878
Release:	2
Summary:	Print Steinmetz notation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/steinmetz
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/steinmetz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/steinmetz.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/steinmetz.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The steinmetz package provides a command for typesetting
complex numbers in the Steinmetz notation used in
electrotechnics as: <modulus><argument or phase inside an angle
symbol> The package makes use of pict2e.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/steinmetz/steinmetz.sty
%doc %{_texmfdistdir}/doc/latex/steinmetz/README
%doc %{_texmfdistdir}/doc/latex/steinmetz/steinmetz-test.tex
%doc %{_texmfdistdir}/doc/latex/steinmetz/steinmetz.pdf
#- source
%doc %{_texmfdistdir}/source/latex/steinmetz/steinmetz.dtx
%doc %{_texmfdistdir}/source/latex/steinmetz/steinmetz.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
