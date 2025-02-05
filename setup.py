from setuptools import setup, find_packages

setup(
    name="my_lib",              # اسم المكتبة
    version="0.1",              # رقم الإصدار
    packages=find_packages(),   # البحث عن جميع الحزم داخل المجلد
    install_requires=[],        # المتطلبات (إذا احتجت مكتبات خارجية)
    author="اسمك",
    author_email="بريدك@example.com",
    description="مكتبة رياضية بسيطة",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_lib",  # رابط GitHub (اختياري)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
