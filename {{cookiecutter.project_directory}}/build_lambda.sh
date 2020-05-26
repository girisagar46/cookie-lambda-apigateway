#!/usr/bin/env bash

# remove function.zip if already exists
rm function.zip

# create package directory (-p for suppressing error if the directory already exists)
mkdir -p package

cd package

# Install packages from requirements.lambda.txt
pip3 install -r ../requirements.lambda.txt --target .

# zip the library dependency
zip -r9 ../function.zip .

cd -

# Add {{ cookiecutter.lambda_file_name }}.py to the zipped folder
zip -g function.zip {{ cookiecutter.lambda_file_name }}.py # TODO: Add other files if any

# Remove the package folder after function.zip is created successfully
rm -rf package
