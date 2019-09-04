%include	/usr/lib/rpm/macros.perl
Summary:	latexmk - generate LaTeX document
Summary(pl.UTF-8):	latexmk - generowanie dokumentów w LaTeXu
Name:		latexmk
# see end of CHANGES file
Version:	4.65
Release:	1
License:	GPL v2
Group:		Applications/Publishing/TeX
Source0:	http://tug.ctan.org/support/latexmk.zip
# Source0-md5:	57f3ea42ba3c0b6dcffe07c640d2b54e
URL:		https://ctan.org/pkg/latexmk
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	texlive-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Latexmk completely automates the process of generating a LaTeX
document. Essentially, it is a highly specialized cousin of the
general make utility. Given the source files for a document, latexmk
issues the appropriate sequence of commands to generate a .dvi, .ps,
.pdf or hardcopy version of the document, including repeated running
of the programs until cross references etc. are resolved. Latexmk can
also be set to run continuously with a previewer; the latex program,
etc., are rerun whenever one of the source files is modified.

%description -l pl.UTF-8
Latexmk całkowicie automatyzuje proces generowania dokumentów w
LaTeXu. Zasadniczo jest to wysoko specjalizowany kuzyn ogólnego
polecenia make. Po podaniu plików źródłowych dokumentu latexmk
wydaje odpowiednią sekwencję poleceń do wygenerowania wersji .dvi,
.ps, .pdf lub wydruku dokumentu, włącznie z powtarzaniem uruchamiania
tych programów aż do rozwiązania odnośników itp.. Latexmk może być
także skonfigurowany do stałego działania wraz z przeglądarką -
program latex itd. są uruchamiane ponownie, kiedy zostanie
zmodyfikowany jakiś plik źródłowy.

%prep
%setup -q -n %{name}

%{__sed} -i '1s,/usr/bin/env perl,%{__perl},' latexmk.pl

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
cp -p latexmk.pl $RPM_BUILD_ROOT%{_bindir}/latexmk
cp -p latexmk.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/latexmk
%{_mandir}/man1/latexmk.1*
