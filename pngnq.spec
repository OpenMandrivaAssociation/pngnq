Name:		pngnq
Summary:	Pngnq is a tool for quantizing PNG images in RGBA format
Version:	1.1
Release:	2
License:	BSD with advertising and MIT and BSD
Group:		Graphics
URL:		http://pngnq.sourceforge.net/
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		pngnq-libpng15.patch
BuildRequires:	pkgconfig(libpng)

%description
Pngnq is a tool for quantizing PNG images in RGBA format.

The neuquant algorithm uses a neural network to optimize the color
map selection. This is fast and quite accurate, giving good results
on many types of images.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README COPYING ChangeLog NEWS
%{_bindir}/*
%{_mandir}/man1/%{name}.*

