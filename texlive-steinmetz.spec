%global tl_name steinmetz
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Print Steinmetz notation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/steinmetz
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/steinmetz.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/steinmetz.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/steinmetz.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The steinmetz package provides a command for typesetting complex numbers
in the Steinmetz notation used in electrotechnics as:
<modulus>;<argument or phase inside an angle symbol> The package makes
use of pict2e.

