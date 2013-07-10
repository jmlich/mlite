# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       mlite

# >> macros
# << macros

Summary:    Useful classes originating from MeeGo Touch
Version:    0.1.5
Release:    1
Group:      System/Libraries
License:    LGPL v2.1
URL:        http://www.meego.com
Source0:    %{name}-%{version}.tar.bz2
Source100:  mlite.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(QtDBus)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(gconf-2.0)

%description
Select set of useful classes from meegotouch that do not require
taking in all of meegotouch.


%package devel
Summary:    mlite development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files needed for using the mlite library


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake  \
    VERSION=%{version}

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libmlite.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/mlite
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libmlite.so
# >> files devel
# << files devel
