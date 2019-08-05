#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

ingredients = []

enter_more = raw_input("Do you have any specific ingredients to enter? [y|n]: ").lower()

while enter_more == "y":
    ingredients.append(raw_input("What is the ingredient? One word only please: ").lower())
    enter_more = raw_input("Do you have any more ingredients to enter? [y|n]: ").lower()

recipe = raw_input("What kind of recipe do you want to find? ")

# Write your code below!
