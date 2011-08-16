Name:		grok
Version:	1.20110630.1
Release:	1%{?dist}
Summary:	Grok is simple software that allows you to easily parse logs and other files.

Group:		unknown
License:	unknown
URL:		https://github.com/jordansissel/grok/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	pcre-devel
BuildRequires:	libevent-devel
BuildRequires:	gperf
BuildRequires:	tokyocabinet-devel

%description
Grok is simple software that allows you to easily parse logs and other files. With grok, you can turn unstructured log and event data into structured data.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/usr/lib  $RPM_BUILD_ROOT/usr/_lib
mv $RPM_BUILD_ROOT/usr/_lib $RPM_BUILD_ROOT/%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin
/usr/include
/usr/share
%{_libdir}

%doc

%changelog
