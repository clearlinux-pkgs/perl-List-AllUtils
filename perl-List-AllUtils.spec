#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-AllUtils
Version  : 0.14
Release  : 11
URL      : http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/List-AllUtils-0.14.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/List-AllUtils-0.14.tar.gz
Summary  : 'Combines List::Util, List::SomeUtils and List::UtilsBy in one bite-sized package'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-List-AllUtils-doc
BuildRequires : perl(Exporter::Tiny)
BuildRequires : perl(List::SomeUtils)
BuildRequires : perl(List::Util)
BuildRequires : perl(List::UtilsBy)

%description
# NAME
List::AllUtils - Combines List::Util, List::SomeUtils and List::UtilsBy in one bite-sized package

%package doc
Summary: doc components for the perl-List-AllUtils package.
Group: Documentation

%description doc
doc components for the perl-List-AllUtils package.


%prep
%setup -q -n List-AllUtils-0.14

%build
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/List/AllUtils.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
