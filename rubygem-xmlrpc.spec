# Generated from xmlrpc-0.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name xmlrpc

Name: rubygem-%{gem_name}
Version: 0.3.1
Release: 1%{?dist}
Summary: XMLRPC is a lightweight protocol that enables remote procedure calls over HTTP
License: Ruby and BSD-2-Clause
URL: https://github.com/ruby/xmlrpc
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
XMLRPC is a lightweight protocol that enables remote procedure calls over
HTTP.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/xmlrpc.gemspec
%{gem_instdir}/NEWS.md

%changelog
* Wed Jan 13 2021 Pavel Valena <pvalena@redhat.com> - 0.3.1-1
- Initial package
