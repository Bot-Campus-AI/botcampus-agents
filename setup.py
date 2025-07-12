from setuptools import setup, find_packages

setup(
    name="botcampus-agents",
    version="0.1",
    packages=find_packages(include=["botcampus*"]),
    install_requires=[
        "openai",
        "python-dotenv"
    ],
    author="BotCampus AI",
    description="A lightweight Python SDK to build and run AI agents using OpenAI.",
    license="MIT",
    url="https://github.com/Bot-Campus-AI/botcampus-agents",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
