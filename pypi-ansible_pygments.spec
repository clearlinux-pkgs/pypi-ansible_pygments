#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ansible_pygments
Version  : 0.1.1
Release  : 11
URL      : https://files.pythonhosted.org/packages/0b/35/53891104863a04f69ff761cccd9b11784e19793cd318ecff8f2e5c594401/ansible-pygments-0.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/0b/35/53891104863a04f69ff761cccd9b11784e19793cd318ecff8f2e5c594401/ansible-pygments-0.1.1.tar.gz
Summary  : Tools for building the Ansible Distribution
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-ansible_pygments-license = %{version}-%{release}
Requires: pypi-ansible_pygments-python = %{version}-%{release}
Requires: pypi-ansible_pygments-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
# [Pygments] lexer and style Ansible snippets
[![GitHub Actions CI/CD workflow](https://github.com/ansible-community/ansible-pygments/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/ansible-community/ansible-pygments/actions/workflows/ci-cd.yml)
[![Codecov badge](https://img.shields.io/codecov/c/github/ansible-community/ansible-pygments)](https://codecov.io/gh/ansible-community/ansible-pygments)

%package license
Summary: license components for the pypi-ansible_pygments package.
Group: Default

%description license
license components for the pypi-ansible_pygments package.


%package python
Summary: python components for the pypi-ansible_pygments package.
Group: Default
Requires: pypi-ansible_pygments-python3 = %{version}-%{release}

%description python
python components for the pypi-ansible_pygments package.


%package python3
Summary: python3 components for the pypi-ansible_pygments package.
Group: Default
Requires: python3-core
Provides: pypi(ansible_pygments)
Requires: pypi(pygments)

%description python3
python3 components for the pypi-ansible_pygments package.


%prep
%setup -q -n ansible-pygments-0.1.1
cd %{_builddir}/ansible-pygments-0.1.1
pushd ..
cp -a ansible-pygments-0.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656355408
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ansible_pygments
cp %{_builddir}/ansible-pygments-0.1.1/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-ansible_pygments/02f46c5154752a0af7d98adae5c78107edf64727
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ansible_pygments/02f46c5154752a0af7d98adae5c78107edf64727

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
