%define is_el4 %(grep -i "release 4" /etc/redhat-release > /dev/null 2>&1 && echo 1 || echo 0)
%define is_el5 %(grep -i "release 5" /etc/redhat-release > /dev/null 2>&1 && echo 1 || echo 0)

Name:           zabbix-jp-release
%if %is_el4
Version:        4
%endif
%if %is_el5
Version:        5
%endif
Release:        3
Summary:        ZABBIX-JP repository configuration

Group:          System Environment/Base
License:        GPL 
URL:            http://www.zabbix.jp

Source0:        http://www.zabbix.jp/rpms/RPM-GPG-KEY-ZABBIX-JP
Source1:        GPL
Source2:        zabbix-jp.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       redhat-release >=  %{version}

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
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}

cat %{SOURCE2} |sed \
    -e 's/{zbxver}/zabbix-1.1/g' \
    > $RPM_BUILD_ROOT%{_datadir}/%{name}/zabbix-jp-1.1.repo
cat %{SOURCE2} |sed \
    -e 's/{zbxver}/zabbix-1.4/g' \
    > $RPM_BUILD_ROOT%{_datadir}/%{name}/zabbix-jp-1.4.repo
cat %{SOURCE2} |sed \
    -e 's/{zbxver}/zabbix-1.6/g' \
    > $RPM_BUILD_ROOT%{_datadir}/%{name}/zabbix-jp-1.6.repo
cat %{SOURCE2} |sed \
    -e 's/{zbxver}/zabbix-1.8/g' \
    > $RPM_BUILD_ROOT%{_datadir}/%{name}/zabbix-jp-1.8.repo

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/alternatives --install /etc/yum.repos.d/zabbix-jp.repo %{name} %{_datadir}/%{name}/zabbix-jp-1.1.repo 10
/usr/sbin/alternatives --install /etc/yum.repos.d/zabbix-jp.repo %{name} %{_datadir}/%{name}/zabbix-jp-1.4.repo 20
/usr/sbin/alternatives --install /etc/yum.repos.d/zabbix-jp.repo %{name} %{_datadir}/%{name}/zabbix-jp-1.6.repo 40
/usr/sbin/alternatives --install /etc/yum.repos.d/zabbix-jp.repo %{name} %{_datadir}/%{name}/zabbix-jp-1.6.repo 30

%preun
/usr/sbin/alternatives --remove %{name} %{_datadir}/%{name}/zabbix-jp-1.1.repo
/usr/sbin/alternatives --remove %{name} %{_datadir}/%{name}/zabbix-jp-1.4.repo
/usr/sbin/alternatives --remove %{name} %{_datadir}/%{name}/zabbix-jp-1.6.repo
/usr/sbin/alternatives --remove %{name} %{_datadir}/%{name}/zabbix-jp-1.8.repo

%files
%defattr(-,root,root,-)
%doc GPL
/etc/pki/rpm-gpg/RPM-GPG-KEY-ZABBIX-JP
%config(noreplace) %{_datadir}/%{name}

%changelog
* Mon Jan 18 2010 Kodai Terashima <kodai74@gmail.com> - 5-3
- Add zabbix 1.8 repository

* Wed Nov 11 2009 Kodai Terashima <kodai74@gmail.com> - 5-2
- Marge RHEL5/CentOS5 and RHEL4/CentOS4 spec file
- Add support for several zabbix version
- Change repository directory

* Tue Jun 16 2009 Kodai Terashima <kodai74@gmail.com> - 5-1
- Initial Package for RHEL5
