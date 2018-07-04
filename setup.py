# -*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
import io

VERSION = '0.1'

with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

install_requires = open("requirements.txt").readlines()

setup(
    name="ecpay_invoice",  # pip 安裝時用的名字
    version=VERSION,  # 當前版本，每次更新上傳到pypi都需要修改
    author="skypc785308",
    author_email="skypc785308@gmail.com",
    url="https://github.com/skypc785308/ecpay_invoice",
    keyworads="zhihu",
    description="zhihu api from humans",
    long_description=long_description,
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    license='MIT License',
    classifiers=[],
    install_requires=install_requires,
)