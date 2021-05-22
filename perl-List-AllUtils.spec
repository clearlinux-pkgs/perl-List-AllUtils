#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-AllUtils
Version  : 0.19
Release  : 37
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-AllUtils-0.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-AllUtils-0.19.tar.gz
Summary  : 'Combines List::Util, List::SomeUtils and List::UtilsBy in one bite-sized package'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-List-AllUtils-license = %{version}-%{release}
Requires: perl-List-AllUtils-perl = %{version}-%{release}
Requires: perl-List-Util
BuildRequires : buildreq-cpan
BuildRequires : perl(Exporter::Tiny)
BuildRequires : perl(List::SomeUtils)
BuildRequires : perl(List::Util)
BuildRequires : perl(List::UtilsBy)

%description
# NAME
List::AllUtils - Combines List::Util, List::SomeUtils and List::UtilsBy in one bite-sized package

%package dev
Summary: dev components for the perl-List-AllUtils package.
Group: Development
Provides: perl-List-AllUtils-devel = %{version}-%{release}
Requires: perl-List-AllUtils = %{version}-%{release}

%description dev
dev components for the perl-List-AllUtils package.


%package license
Summary: license components for the perl-List-AllUtils package.
Group: Default

%description license
license components for the perl-List-AllUtils package.


%package perl
Summary: perl components for the perl-List-AllUtils package.
Group: Default
Requires: perl-List-AllUtils = %{version}-%{release}

%description perl
perl components for the perl-List-AllUtils package.


%prep
%setup -q -n List-AllUtils-0.19
cd %{_builddir}/List-AllUtils-0.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-List-AllUtils
cp %{_builddir}/List-AllUtils-0.19/LICENSE %{buildroot}/usr/share/package-licenses/perl-List-AllUtils/b8b06ed4b81cb502701ecd70f6cebc7947bffabf
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::AllUtils.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-List-AllUtils/b8b06ed4b81cb502701ecd70f6cebc7947bffabf

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/List/AllUtils.pm
