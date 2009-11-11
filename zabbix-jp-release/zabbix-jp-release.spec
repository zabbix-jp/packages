Name:           zabbix-jp-release       
Version:        5 
Release:        1
Summary:        ZABBIX-JP repository configuration

Group:          System Environment/Base 
License:        GPL 
URL:            http://www.zabbix.jp

Source0:        http://www.zabbix.jp/rpms/RPM-GPG-KEY-ZABBIX-JP
Source1:        GPL
Source2:        zabbix-jp.repo	

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:      redhat-release >=  %{version} 

%description
This package contains the ZABBIX-JP repository
GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ZABBIX-JP

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*


%changelog
* Tue Jun 16 2009 Kodai Terashima <kodai74@gmail.com> - 5-1
- Initial Package for RHEL5
