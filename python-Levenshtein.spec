%define 	module		Levenshtein
%define 	egg_name	python_Levenshtein
%define		pypi_name	python-Levenshtein
Summary:	Python extension computing string distances and similarities
Summary(pl.UTF-8):	Rozszerzenie Pythona do obliczania odległości i podobieństw łańcuchów
Name:		python-%{module}
Version:	0.12.0
Release:	11
License:	GPL v2
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	e8cde197d6d304bbdc3adae66fec99fb
URL:		https://github.com/ztane/python-Levenshtein/
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Levenshtein computes Levenshtein distances, similarity ratios,
generalized medians and set medians of Strings and Unicodes. Becuase
it's implemented in C, it's much faster than corresponding Python
library functions and methods.

%description -l pl.UTF-8
Levenshtein oblicza odległości Levenshteina, współczynniki
podobieństwa, uogólnione mediany i mediany zbiorów dla wartości String
i Unicode. Ponieważ jest zaimplementowany w C, jest dużo szybszy od
odpowiadających mu funkcji bibliotecznych i metod Pythona.

%package -n python3-%{module}
Summary:	Python extension computing string distances and similarities
Summary(pl.UTF-8):	Rozszerzenie Pythona do obliczania odległości i podobieństw łańcuchów
Group:		Libraries/Python

%description -n python3-%{module}
Levenshtein computes Levenshtein distances, similarity ratios,
generalized medians and set medians of Strings and Unicodes. Becuase
it's implemented in C, it's much faster than corresponding Python
library functions and methods.

%description -n python3-%{module} -l pl.UTF-8
Levenshtein oblicza odległości Levenshteina, współczynniki
podobieństwa, uogólnione mediany i mediany zbiorów dla wartości String
i Unicode. Ponieważ jest zaimplementowany w C, jest dużo szybszy od
odpowiadających mu funkcji bibliotecznych i metod Pythona.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install
%py_postclean

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/%{module}/_levenshtein.[ch]

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst NEWS HISTORY.txt
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/_levenshtein.so
%{py_sitedir}/%{egg_name}-%{version}-py*.egg-info
