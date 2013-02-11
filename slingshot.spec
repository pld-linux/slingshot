Summary:	Slingshot is a lightweight and stylish app launcher for Pantheon and other DEs
Name:		slingshot
Version:	0.7
Release:	0.1
License:	GPL v3
Group:		X11/Applications
#Source0:	https://launchpad.net/slingshot/trunk/0.6/+download/%{name}-%{version}.tar.bz2
Source0:	https://launchpad.net/slingshot/0.x/0.7/+download/%{name}-%{version}.tar.gz
# Source0-md5:	25be09dc150194216d3ee22de8fa8ffe
URL:		https://launchpad.net/slingshot
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	granite-devel
#BuildRequires:	granite-devel >= 0.1.3
BuildRequires:	gtk+3-devel >= 3.2.0
BuildRequires:	libgee0.6-devel
BuildRequires:	libunity-devel
BuildRequires:	libwnck-devel
BuildRequires:	libzeitgeist-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	vala >= 0.10.0
BuildRequires:	vala-zeitgeist
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Slingshot is an app launcher created specifically for elementary, but
is usable with other desktop environments as well.

It's supposed to be simple, easy on the eyes and just works without
much pc knowledge or explanation.

%prep
%setup -qc

%{__sed} -i -e 's,libgnome-menu;,libgnome-menu-3.0;,' CMakeLists.txt

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/rue
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/sma

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
