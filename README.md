<p align="center">
  <img src="static/imgs/eraser.png" width="20%" alt="CLEARCANVAS-logo"
  style="background-color: white; border-radius: 5px;">
</p>
<p align="center">
    <h1 align="center">CLEARCANVAS</h1>
</p>
<p align="center">
    <em><code>❯ Ved patel, Krish Harish, Arsh Bhalala</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/ved-patel226/ClearCanvas-Congressional-App-Challenge-24?style=flat&logo=opensourceinitiative&logoColor=white&color=705c53" alt="license">
	<img src="https://img.shields.io/github/last-commit/ved-patel226/ClearCanvas-Congressional-App-Challenge-24?style=flat&logo=git&logoColor=white&color=705c53" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/ved-patel226/ClearCanvas-Congressional-App-Challenge-24?style=flat&color=705c53" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/ved-patel226/ClearCanvas-Congressional-App-Challenge-24?style=flat&color=705c53" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>

<br>

##### 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
    - [🔖 Prerequisites](#-prerequisites)
    - [📦 Installation](#-installation)
    - [🤖 Usage](#-usage)
    - [🧪 Tests](#-tests)
- [📌 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

<code>❯ ClearCanvas is a software for students to report problems in their school. ClearCanvas can solve problems from sharing math answers to vaping.</code>

---

## 👾 Features

<code>❯ Pin system for easily selecting the location of the issue</code>

<code>❯ Ask questions easier with email integration</code>

<code>❯ Find schools easily with our school-finder</code>

---

## 📂 Repository Structure

```sh
└── ClearCanvas/
    ├── main.py
    ├── py_tools
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── essentials
    │   └── misc
    ├── static
    │   ├── js
    │   ├── school-maps
    │   ├── schools
    │   ├── styles
    │   └── svgs
    └── templates
        ├── base.html
        ├── dashboard.html
        ├── error.html
        ├── index.html
        ├── login.html
        ├── problem.html
        ├── problems.html
        ├── register.html
        └── success.html
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File | Summary |
| --- | --- |
| [main.py](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/main.py) | <code>Main python file for the flask app</code> |

</details>

<details closed><summary>templates</summary>

| File | Summary |
| --- | --- |
| [register.html](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/templates/register.html) | <code>❯ HTML file for registering schools</code> |
| [success.html](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/templates/success.html) | <code>❯ HTML file for the success message</code> |
| [problem.html](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/templates/problem.html) | <code>❯ HTML file for viewing the file</code> |
| [error.html](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/templates/error.html) | <code>❯ HTML file for errors</code> |
| [login.html](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/templates/login.html) | <code>❯ HTML file for student/teacher login</code> |
| [index.html](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/templates/index.html) | <code>❯ HTML file for the landing page</code> |
| [base.html](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/templates/base.html) | <code>❯ Base HTML file for all html files</code> |
| [dashboard.html](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/templates/dashboard.html) | <code>❯ HTML file for teachers'/students' dashboard</code> |
| [problems.html](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/templates/problems.html) | <code>❯ HTML file for viewing all problems</code> |

</details>

<details closed><summary>py_tools.essentials</summary>

| File | Summary |
| --- | --- |
| [mongo_db.py](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/py_tools/essentials/mongo_db.py) | <code>❯ Python file to make communication between Mongo and us easier</code> |
| [env_to_var.py](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/py_tools/essentials/env_to_var.py) | <code>❯ Python file for getting API keys from .env file</code> |

</details>

<details closed><summary>py_tools.misc</summary>

| File | Summary |
| --- | --- |
| [latest.py](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/py_tools/misc/latest.py) | <code>❯ Python file for getting the latest timestamp</code> |
| [school_searcher.py](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/py_tools/misc/school_searcher.py) | <code>❯ Python file for finding your school from the csv</code> |
| [send_email.py](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/py_tools/misc/send_email.py) | <code>❯ Python file for sending emails (scrapped due to time)</code> |
| [school_info.py](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/py_tools/misc/school_info.py) | <code>❯ Python file for getting school info from MongoDB</code> |

</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

**Python**: `Version: 3.10`

### 📦 Installation

Build the project from source:

1. Clone the ClearCanvas repository:
```sh
❯ git clone https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24
```

2. Navigate to the project directory:
```sh
❯ cd ClearCanvas-Congressional-App-Challenge-24
```

3. Install the required dependencies. **<span style="color: red;">WE RECOMMEND USING CONDA</span>**
```sh
❯ ❯ pip install -r requirements.txt
```


### 🤖 Usage

To run the project, execute the following command:

```sh
❯ ❯ python3 main.py
```

---

## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Release V1.0</strike>
- [ ] **`Task 2`**: Add auto-email support.\
- [ ] **`Task 3`**: Add mobile support

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/issues)**: Submit bugs found or log feature requests for the `ClearCanvas` project.
- **[Submit Pull Requests](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/ved-patel226/ClearCanvas-Congressional-App-Challenge-24
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/ved-patel226/ClearCanvas-Congressional-App-Challenge-24/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=ved-patel226/ClearCanvas-Congressional-App-Challenge-24">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
