%define name	pngnq
%define version	1.1
%define release	1

Name:		%{name}
Summary:	Pngnq is a tool for quantizing PNG images in RGBA format
Version:	%{version}
Release:	%mkrel %{release}
License:	BSD with advertising and MIT and BSD
Group:		Graphics
URL:		http://pngnq.sourceforge.net/
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	png-devel

%description
Pngnq is a tool for quantizing PNG images in RGBA format.

The neuquant algorithm uses a neural network to optimize the color
map selection. This is fast and quite accurate, giving good results
on many types of images.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING ChangeLog NEWS
%{_bindir}/*
%{_mandir}/man1/%{name}.*
