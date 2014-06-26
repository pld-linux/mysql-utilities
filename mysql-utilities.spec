Summary:	Scripts for managing and administering MySQL servers
Name:		mysql-utilities
Version:	1.4.3
Release:	1
License:	GPL v2
Group:		Applications/Databases
Source0:	http://cdn.mysql.com/Downloads/MySQLGUITools/%{name}-%{version}.tar.gz
# Source0-md5:	bfe86977134c453bbe914e387121775f
Patch1:		paths.patch
URL:		http://dev.mysql.com/downloads/utilities/
BuildRequires:	python-Sphinx >= 1.0
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
Requires:	python-mysql-connector >= 1.0.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL Utilities provides a collection of command-line utilities that
are used for maintaining and administering MySQL servers, including:

- Admin Utilities (Clone, Copy, Compare, Diff, Export, Import)
- Replication Utilities (Setup, Configuration)
- General Utilities (Disk Usage, Redundant Indexes, Search Meta Data)

%prep
%setup -q
v=$(head -n1 CHANGES.txt | awk '{print $2}')
test "$v" = "%{version}"

%patch1 -p1

# you'll need this if you cp -a complete dir in source
# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install_man install \
	--skip-profile \
	--root $RPM_BUILD_ROOT

# packaged by python-mysql-connector
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/mysql/__init__.py*
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/mysql/connector

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/mysqlauditadmin
%attr(755,root,root) %{_bindir}/mysqlauditgrep
%attr(755,root,root) %{_bindir}/mysqldbcompare
%attr(755,root,root) %{_bindir}/mysqldbcopy
%attr(755,root,root) %{_bindir}/mysqldbexport
%attr(755,root,root) %{_bindir}/mysqldbimport
%attr(755,root,root) %{_bindir}/mysqldiff
%attr(755,root,root) %{_bindir}/mysqldiskusage
%attr(755,root,root) %{_bindir}/mysqlfabric
%attr(755,root,root) %{_bindir}/mysqlfailover
%attr(755,root,root) %{_bindir}/mysqlfrm
%attr(755,root,root) %{_bindir}/mysqlindexcheck
%attr(755,root,root) %{_bindir}/mysqlmetagrep
%attr(755,root,root) %{_bindir}/mysqlprocgrep
%attr(755,root,root) %{_bindir}/mysqlreplicate
%attr(755,root,root) %{_bindir}/mysqlrpladmin
%attr(755,root,root) %{_bindir}/mysqlrplcheck
%attr(755,root,root) %{_bindir}/mysqlrplms
%attr(755,root,root) %{_bindir}/mysqlrplshow
%attr(755,root,root) %{_bindir}/mysqlrplsync
%attr(755,root,root) %{_bindir}/mysqlserverclone
%attr(755,root,root) %{_bindir}/mysqlserverinfo
%attr(755,root,root) %{_bindir}/mysqluc
%attr(755,root,root) %{_bindir}/mysqluserclone
%{_mandir}/man1/mysqlauditadmin.1*
%{_mandir}/man1/mysqlauditgrep.1*
%{_mandir}/man1/mysqldbcompare.1*
%{_mandir}/man1/mysqldbcopy.1*
%{_mandir}/man1/mysqldbexport.1*
%{_mandir}/man1/mysqldbimport.1*
%{_mandir}/man1/mysqldiff.1*
%{_mandir}/man1/mysqldiskusage.1*
%{_mandir}/man1/mysqlfailover.1*
%{_mandir}/man1/mysqlindexcheck.1*
%{_mandir}/man1/mysqlmetagrep.1*
%{_mandir}/man1/mysqlprocgrep.1*
%{_mandir}/man1/mysqlreplicate.1*
%{_mandir}/man1/mysqlrpladmin.1*
%{_mandir}/man1/mysqlrplcheck.1*
%{_mandir}/man1/mysqlrplshow.1*
%{_mandir}/man1/mysqlserverclone.1*
%{_mandir}/man1/mysqlserverinfo.1*
%{_mandir}/man1/mysqluc.1*
%{_mandir}/man1/mysqluserclone.1*

%dir %{py_sitescriptdir}/mysql/utilities
%{py_sitescriptdir}/mysql/utilities/*.py[co]
%dir %{py_sitescriptdir}/mysql/utilities/command
%{py_sitescriptdir}/mysql/utilities/command/*.py[co]
%dir %{py_sitescriptdir}/mysql/utilities/common
%{py_sitescriptdir}/mysql/utilities/common/*.py[co]
%{py_sitescriptdir}/mysql/fabric
%{py_sitescriptdir}/mysql_utilities-*.egg-info
