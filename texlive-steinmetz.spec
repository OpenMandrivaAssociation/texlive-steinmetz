# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/steinmetz
# catalog-date 2009-11-10 00:30:52 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-steinmetz
Version:	1.0
Release:	1
Summary:	Print Steinmetz notation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/steinmetz
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/steinmetz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/steinmetz.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/steinmetz.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The steinmetz package provides a command for typesetting
complex numbers in the Steinmetz notation used in
electrotechnics as: <modulus><argument or phase inside an angle
symbol> The package makes use of pict2e.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
