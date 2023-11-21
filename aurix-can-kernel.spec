# If kversion isn't defined on the rpmbuild line, define it here.
%{!?kversion: %define kversion %(uname -r)}

%define kmod_name aurix-can

%define debug_package %{nil}

Summary: Unified driver for Aurix CAN controllers
Name: aurix-can
Version: 1.0
Release: r0_sa8775
License: GPL-2.0
URL: https://git.codelinaro.org/
Source0:%{name}-%{version}.tar.gz
BuildRequires:  kernel-automotive-devel-uname-r = %{kversion} make libtool gcc-g++ systemd-rpm-macros
Requires: kernel-automotive-core-uname-r = %{kversion}

%description
This adds unified driver for Aurix CAN controllers on auto Platform. This
driver can support a few Uart controllers being used on automotive
paltform. This Driver uses uart bus to comunicate with Aurix can.

%package -n kernel-module-aurix-can-5.14.0-rt21
Summary: aurix-can kernel module
License: GPL-2.0

%description -n kernel-module-aurix-can-5.14.0-rt21
aurix-can kernel module; AURIX CAN controller module

%prep
%setup -qn %{name}

%build
#%make_build
KSRC=%{_usrsrc}/kernels/%{kversion}
make KERNEL_SRC=${KSRC} modules

%post
depmod %{kversion}

%postun
depmod %{kversion}

%install
KSRC=%{_usrsrc}/kernels/%{kversion}
make KERNEL_SRC=${KSRC} INSTALL_MOD_PATH=$RPM_BUILD_ROOT  modules_install
rm -rf "$RPM_BUILD_ROOT/lib/modules/%{kversion}/modules."*

%clean
rm -rf $RPM_BUILD_ROOT

%files
/lib/modules/%{kversion}/extra/aurix-can.ko
