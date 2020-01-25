#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%define		pdir	Curses
%define		pnam	Forms
Summary:	Curses::Forms - Curses Forms Framework
Summary(pl.UTF-8):	Curses::Forms - szkielet formularzy oparty na bibliotece curses
Name:		perl-Curses-Forms
Version:	1.997
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Curses/CursesForms-%{version}.tar.gz
# Source0-md5:	076faf4c240d4577720a7bd2bc1d3f04
URL:		http://search.cpan.org/dist/CursesForms/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Curses
BuildRequires:	perl-Curses-Widgets
%if %{with tests}
BuildRequires:	perl-Test-Pod
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Curses::Forms Perl module is a UI framework based on the curses
library. It can be used for the development of curses based user
interfaces. Strictly this a wrapper around Curses::UI and
Curses::Widgets to create simple UIs quickly.

%description -l pl.UTF-8
Moduł Perla Curses::Forms stanowi szkielet interfejsu użytkownika
oparty na bibliotece curses. Może służyć do konstruowania interfejsów
użytkownika w oparciu o bibliotekę curses. Dokładniej, Curses::Forms
to wrapper do Curses::UI i Curses::Widgets, ułatwiający tworzenie
prostych GUI.

%prep
%setup -q -n CursesForms-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# get rid of pod documentation
#rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Curses/Forms/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{perl_vendorlib}/Curses/Forms.pm
%{perl_vendorlib}/Curses/Forms
%{_mandir}/man3/*
