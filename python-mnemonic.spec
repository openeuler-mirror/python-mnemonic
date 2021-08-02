Name:      python-mnemonic
Version:   0.19
Release:   1
Summary:   Implementation of Bitcoin BIP-0039

License:   MIT
URL:       https://github.com/trezor/python-mnemonic
Source0:   https://github.com/trezor/python-mnemonic/archive/refs/tags/v0.19.tar.gz

BuildArch: noarch

%description
This BIP describes the implementation of a mnemonic code or mnemonic sentence -
a group of easy to remember words - for the generation of deterministic wallets.

%package -n python3-mnemonic
Summary:        Implementation of Bitcoin BIP-0039
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-mnemonic 
This BIP describes the implementation of a mnemonic code or mnemonic sentence -
a group of easy to remember words - for the generation of deterministic wallets.

%prep
%autosetup -n mnemonic-0.19
rm -rf mnemonic.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-mnemonic
%doc PKG-INFO
%doc README.rst
%license LICENSE
%{python3_sitelib}/mnemonic-*.egg-info/
%{python3_sitelib}/mnemonic/

%changelog
* Wed Jul 07 2021 liuzhaoyang <liuzhaoyang@kylinos.cn> - 0.19-1
- Initial package