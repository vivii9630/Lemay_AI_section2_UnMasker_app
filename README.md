<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Unmasker webapp, Lemay-AI, secttion2</h3>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The project is about creating a Flask API appication with JSON object. Additionally, we have included pretrained transformer of 'fill-mask' AI model from transformer pipeline for unmasking the words in messages. 

The objective of the project includes,
* API interface in REST vocab about messages.
* Automatic unmasking of possible tokens in the message.
* Building AI model interface through API.

Model is loaded from: https://huggingface.co/bert-base-uncased. The reason to choose this model is that, being familiar with RNN's in predicting the next token based on maximum likehood estimation, the (t+1)th token is forseen by the RNN's as well as the (t+1)th is also from the same vocab. However, BERT models are specifically employed for predicting the masked words as they are learned bidirectionally. I took this chance to know more about BERT and it's variants including RoBERTA, DistilBERT etc.  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Results and additional feature implemented for efficient production:
#### Postman testing results:
![](https://github.com/vivii9630/Lemay_AI_section2_UnMasker_app/blob/main/images/postman_result.gif)
<br></br>

#### Making request to the app:
- Received response as a generator object.
- Created an iterator (generator object of the response).

![](https://github.com/vivii9630/Lemay_AI_section2_UnMasker_app/blob/main/images/request.gif)
<br> </br>
#### Multi threading with flask-python:
- Background process to be handled by threads.
- Thread pool/ Multiple threads
- Concurrency/parallel request handling.
- load balancing

![](https://github.com/vivii9630/Lemay_AI_section2_UnMasker_app/blob/main/images/threadpool1.png)
![](https://github.com/vivii9630/Lemay_AI_section2_UnMasker_app/blob/main/images/threadpool2.png)
### Built With

* [![Flask][Flask.com]][Flask-url]
* [![HuggingFace-model][Huggingface.co]][Huggingface-url]
* [![Docker][Docker.com]][Docker-url]
* [![Postman][Postman.com]][Postman-url]
* [![Threading][Threading.com]][Threading-url]
* [![PyTorch][Pytorch.com]][Pytorch-url]
* [![PyPi][Pip.com]][Pip-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Before we get started, make sure that, the following is ready. 
- PyTorch transformer, Flask, Pip, docker
- Postman (tesing) - Postman desktop agent.
Create a python venv and install the requirements.
  ```sh
  pip install -r requirements.txt
  ```
This is an example of how to list things you need to use the software and how to install them.

* Docker compose at cli. Navigate to the directory where docker-compose.yaml file is located and execute the following command.
  ```sh
  docker-compose up.
  ```
* However, it recommended to build image and launch the container. Navigate to the directory where Dockerfile is located inside app and execute the following commands.
  ```sh
  docker build -t [NAME] .
  ```
  * Start docker container
  ```sh
  docker run -p [host_port]:[EXPOSE_port] [NAME]
  ```
  The docker container will start running at localserver, however, as the docker container's IP address in windows is different to that of the linux, it is recommendedto run ipconfig at windows cmd terminal to fetch, ethernet adapter vethernet (IPAddress - 192.x.x.x:yyyy).
  
 
It possible to run locally using flask, by navigative to app folder,  
  * Flask
  ```sh
  set FLASK_APP=wsgi.py
  ```
  Kindly reach out to me, incase of issues with the project.



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Vivek Suresh Raj - vivek.sureshraj@ucalgary.ca

Project Link: [(https://github.com/vivii9630/Lemay_AI_section2_UnMasker_app)](https://github.com/vivii9630/Lemay_AI_section2_UnMasker_app)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[docs-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[docs-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Flask.com]:https://img.shields.io/badge/Flask-563D7C?style=for-the-badge&logo=flask&logoColor=green
[Flask-url]:https://flask.palletsprojects.com/en/2.2.x/
[Docker.com]:https://img.shields.io/badge/Docker-563D7C?style=for-the-badge&logo=docker&logoColor=blue
[Docker-url]:https://www.docker.com/
[Huggingface.co]:https://img.shields.io/badge/HuggingFace-563D7C?style=for-the-badge&logo=huggingface&logoColor=yellow
[Huggingface-url]:https://huggingface.co/
[Flask-restful.com]:https://img.shields.io/badge/Flask-restful-563D7C?style=for-the-badge&logo=flask-restful&logoColor=white
[Flask-restful-url]:https://flask-restful.readthedocs.io/en/latest/
[Postman.com]:https://img.shields.io/badge/Postman-563D7C?style=for-the-badge&logo=postman&logoColor=FF3E00
[Postman-url]:https://www.postman.com/
[Threading.com]:https://img.shields.io/badge/Threading-563D7C?style=for-the-badge&logo=threading&logoColor=61DAFB
[Threading-url]:https://docs.python.org/3/library/threading.html
[Pytorch.com]:https://img.shields.io/badge/PyTorch-563D7C?style=for-the-badge&logo=pytorch&logoColor=61DAFB
[Pytorch-url]:https://pytorch.org/get-started/locally/
[Pip.com]:https://img.shields.io/badge/Pip-563D7C?style=for-the-badge&logo=pip&logoColor=61DAFB
[Pip-url]:https://pypi.org/project/pip/
