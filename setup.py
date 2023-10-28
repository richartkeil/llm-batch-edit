from setuptools import setup

setup(
    name='llm-bulk-change',
    version='0.1.0',
    py_modules=['main'],
    install_requires=[
        'click',
        'openai>=1.0.0b', # Using pre-release version for new API.
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'llm-bulk-change = main:run',
        ],
    },
)
