#%define __requires_exclude ^(pear\\(Auth.*|pear\\(PHPUnit.*|pear\\(config.*)$

Name:           osTicket
Version:        1.10
Release:        1%{?dist}
Summary:        Web-based MP3/Ogg/RM/Flac/WMA/M4A manager
License:        AGPLv3+
Group:          Networking/WWW
URL:            http://osticket.com
Source0:        http://osticket.com/sites/default/files/download/%{name}-v%{version}.zip
Requires:	php-imap
Requires:       php-fpm
Requires:       php-mbstring
Requires:       php-mysql
Requires:       php-gd
BuildArch:      noarch

%description
osTicket is a widely-used and trusted open source support ticket system. 
It seamlessly routes inquiries created via email, web-forms and phone 
calls into a simple, easy-to-use, multi-user, web-based customer support 
platform. osTicket comes packed with more features and tools than most 
of the expensive (and complex) support ticket systems on the market.

%prep
mkdir %{name}-%{version}
cd %{name}-%{version}
unzip %{SOURCE0}

%build
# Nothing to do!!

%install
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -r %{name}-%{version}/* %{buildroot}%{_datadir}/%{name}

# apache configuration
install -d -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{name}.conf<<EOF
# Ampache configuration

Alias /%{name} %{_datadir}/%{name}
<Directory %{_datadir}/%{name}>
    Require all granted
    php_admin_value post_max_size 110M
    php_admin_value upload_max_filesize 100M
</Directory>
EOF

%files
%doc %{name}-%{version}/docs/*
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
#%dir %attr(0750,apache,apache) %{_datadir}/%{name}/config
#%dir %attr(0750,apache,apache) %{_datadir}/%{name}/channel
#%dir %attr(0750,apache,apache) %{_datadir}/%{name}/rest
#%dir %attr(0750,apache,apache) %{_datadir}/%{name}/play


%changelog
* Sat Apr 01 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 1.10
- First release of osTicket
