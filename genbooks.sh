#!/bin/zsh

quarto render --profile book,student --output-dir build-book-student
quarto render --profile book,instructor --output-dir build-book-instructor
quarto render --profile projects,student --output-dir build-projects-student
quarto render --profile projects,instructor --output-dir build-projects-instructor