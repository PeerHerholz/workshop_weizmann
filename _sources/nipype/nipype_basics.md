# Basic concepts

After seeing some short examples and showcases of `Nipype`, it's time to check things out more in-depth.

<img src="https://nipype.readthedocs.io/en/latest/_images/nipype_architecture_overview2.png" align="right" alt="workshop logo" width="200" style="margin:0 0 0 0"/>

`Nipype` consists of many parts, but the main ones are `Interfaces`, the `Workflow Engine` with `nodes` and `workflows`, as well as the `Execution Plugins`.
Here's what they are in short:

`Interface`: Wraps a program or function

`Node/MapNode`: Wraps an Interface for use in a Workflow

`Workflow`: A graph or forest of graphs whose edges represent 
                  data flow

`Plugin`: A component that describes how a Workflow should 
             be executed


These and more `building blocks` of `nipype` are explained in the `notebooks` you can find in `ToC` on the left. All of them also include some exercises to help you get some experience and hopefully gain a better understanding. 



