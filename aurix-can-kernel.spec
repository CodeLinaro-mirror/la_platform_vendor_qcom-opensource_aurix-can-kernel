# If kversion isn't defined on the rpmbuild line, define it here.
%{!?kversion: %define kversion %(uname -r)}

%{!?with_oot_debug:  %define with_oot_debug   0}

%define kmod_name aurix-can

%define debug_package %{nil}

%if %{with_oot_debug}
    %define kpackage kernel-automotive-debug
    %define kversion_with_debug %{kversion}+debug
%else
    %define kversion_with_debug %{kversion}
    %define kpackage kernel-automotive
%endif


Summary: Unified driver for Aurix CAN controllers
Name: aurix-can
Version: 1.0
Release: r0_sa8775
License: GPL-2.0
URL: https://git.codelinaro.org/
Source0:%{name}-%{version}.tar.gz
BuildRequires: make libtool gcc-g++ systemd-rpm-macros
BuildRequires: kernel-automotive-devel-uname-r = %{kversion_with_debug}
Requires: %{kpackage}-core-uname-r = %{kversion_with_debug}


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
KSRC=%{_usrsrc}/kernels/%{kversion_with_debug}
make KERNEL_SRC=${KSRC} modules

%post
depmod %{kversion_with_debug}

%postun
depmod %{kversion_with_debug}

%install
KSRC=%{_usrsrc}/kernels/%{kversion_with_debug}
make KERNEL_SRC=${KSRC} INSTALL_MOD_PATH=$RPM_BUILD_ROOT  modules_install
rm -rf "$RPM_BUILD_ROOT/lib/modules/%{kversion_with_debug}/modules."*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%define kernel_module_path /lib/modules/%{kversion_with_debug}
%{kernel_module_path}/extra/aurix-can.ko
