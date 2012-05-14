# NOTE: Not yet published (currently bundled with mysql-workbench),
Summary:	Scripts for managing and administering MySQL servers
Name:		mysql-utilities
Version:	1.0.5
Release:	1
License:	GPL v2
Group:		Applications/Databases
Source0:	ftp://ftp.mirrorservice.org/sites/ftp.mysql.com/Downloads/MySQLGUITools/mysql-workbench-gpl-5.2.39-src.tar.gz
# Source0-md5:	35472b00d48a82d1d13954aef4f916fa
Patch0:		mu-man.patch
URL:		https://code.launchpad.net/mysql-utilities
BuildRequires:	python-Sphinx >= 1.0
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.566
Requires:	python-mysql-connector
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL Utilities contain a collection of scripts useful for managing
and administering MySQL servers.

%prep
%setup -qc
mv mysql-workbench-gpl-*-src/ext/%{name}/* .
%patch0 -p1

%build
v=$(head -n1 CHANGES.txt | awk '{print $2}')
test "$v" = "%{version}"
%{__python} setup.py build_man

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1
%{__python} setup.py install \
	--skip-profile \
	--root $RPM_BUILD_ROOT

# packaged by python-mysql-connector
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/mysql/__init__.py*

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/mysqldbcompare
%attr(755,root,root) %{_bindir}/mysqldbcopy
%attr(755,root,root) %{_bindir}/mysqldbexport
%attr(755,root,root) %{_bindir}/mysqldbimport
%attr(755,root,root) %{_bindir}/mysqldiff
%attr(755,root,root) %{_bindir}/mysqldiskusage
%attr(755,root,root) %{_bindir}/mysqlfailover
%attr(755,root,root) %{_bindir}/mysqlindexcheck
%attr(755,root,root) %{_bindir}/mysqlmetagrep
%attr(755,root,root) %{_bindir}/mysqlprocgrep
%attr(755,root,root) %{_bindir}/mysqlreplicate
%attr(755,root,root) %{_bindir}/mysqlrpladmin
%attr(755,root,root) %{_bindir}/mysqlrplcheck
%attr(755,root,root) %{_bindir}/mysqlrplshow
%attr(755,root,root) %{_bindir}/mysqlserverclone
%attr(755,root,root) %{_bindir}/mysqlserverinfo
%attr(755,root,root) %{_bindir}/mysqluserclone
%{_mandir}/man1/mut.1*
%{_mandir}/man1/mysqldbcompare.1*
%{_mandir}/man1/mysqldbcopy.1*
%{_mandir}/man1/mysqldbexport.1*
%{_mandir}/man1/mysqldbimport.1*
%{_mandir}/man1/mysqldiff.1*
%{_mandir}/man1/mysqldiskusage.1*
%{_mandir}/man1/mysqlindexcheck.1*
%{_mandir}/man1/mysqlmetagrep.1*
%{_mandir}/man1/mysqlprocgrep.1*
%{_mandir}/man1/mysqlreplicate.1*
%{_mandir}/man1/mysqlrplcheck.1*
%{_mandir}/man1/mysqlrplshow.1*
%{_mandir}/man1/mysqlserverclone.1*
%{_mandir}/man1/mysqlserverinfo.1*
%{_mandir}/man1/mysqluserclone.1*

%dir %{py_sitescriptdir}/mysql/utilities
%{py_sitescriptdir}/mysql/utilities/*.py[co]
%dir %{py_sitescriptdir}/mysql/utilities/command
%{py_sitescriptdir}/mysql/utilities/command/*.py[co]
%dir %{py_sitescriptdir}/mysql/utilities/common
%{py_sitescriptdir}/mysql/utilities/common/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/mysql_utilities-*.egg-info
%endif
