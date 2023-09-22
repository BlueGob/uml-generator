<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPLv3 License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
<!--   <a href="https://github.com/BlueGob/uml-generator">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">UML Generator</h3>

  <p align="center">
  A simple web app to generate uml diagrams with some input fields and checkboxes 
    <br />
    <a href="https://github.com/BlueGob/uml-generator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/BlueGob/uml-generator">View Demo</a>
    ·
    <a href="https://github.com/BlueGob/uml-generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/BlueGob/uml-generator/issues">Request Feature</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project
This project is a tool for generating PlantUML code to create diagrams from user-provided input fields and selected checkboxes.
It simplifies the process of creating diagrams by allowing users to define elements and relationships through a user-friendly interface.  


### Built With

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

Python 3.10 installed on your system.<br>
plantUml server running on your machine. check this [link](https://github.com/plantuml/plantuml-server) to install plantuml server locally 
### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
    ```
2. Create venv
   ```sh
   cd uml-generator
   python3 -m venv .venv
   ```
3. Install requirements
   ```sh
   pip install -r requirements.txt
   pip install streamlit-tree-select-0.0.5/
   ```
4. run
   ```
   streamlit run main.py
   ```

<!-- ROADMAP -->
## Roadmap

- [x] use case diagrams
- [ ] class diagram
- [ ] sequence diagram


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GPL 3.0 License. See `LICENSE.txt` for more information.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Othneildrew](https://github.com/othneildrew/Best-README-Template)
* [Schluca](https://github.com/Schluca/streamlit_tree_select)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/BlueGob/uml-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/BlueGob/uml-generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BlueGob/uml-generator.svg?style=for-the-badge
[forks-url]: https://github.com/BlueGob/uml-generator/network/members
[stars-shield]: https://img.shields.io/github/stars/BlueGob/uml-generator.svg?style=for-the-badge
[stars-url]: https://github.com/BlueGob/uml-generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/BlueGob/uml-generator.svg?style=for-the-badge
[issues-url]: https://github.com/BlueGob/uml-generator/issues
[license-shield]: https://img.shields.io/github/license/BlueGob/uml-generator.svg?style=for-the-badge
[license-url]:https://github.com/BlueGob/uml-generator/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
