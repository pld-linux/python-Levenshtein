%define		pname Levenshtein
Summary:	Python extension computing string distances and similarities
Summary(pl):	Rozszerzenie Pythona do obliczania odleg�o�ci i podobie�stw �a�cuch�w
Name:		python-%{pname}
Version:	0.10
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://trific.ath.cx/Ftp//python/levenshtein/python-Levenshtein-0.10.tar.bz2
# Source0-md5:	88d39338fc75090da78adf43785c71b4
URL:		http://trific.ath.cx/resources/python/levenshtein/
BuildRequires:	python-devel >= 1:2.3.0
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Levenshtein computes Levenshtein distances, similarity ratios,
generalized medians and set medians of Strings and Unicodes. Becuase
it's implemented in C, it's much faster than corresponding Python
library functions and methods.

%description -l pl
Levenshtein oblicza odleg�o�ci Levenshteina, wsp�czynniki
podobie�stwa, uog�lnione mediany i mediany zbior�w dla warto�ci String
i Unicode. Poniewa� jest zaimplementowany w C, jest du�o szybszy od
odpowiadaj�cych mu funkcji bibliotecznych i metod Pythona.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{py_sitedir}/%{pname}.so
