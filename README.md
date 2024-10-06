# Final-Project-Template
<!-- Edit the title above with your project title -->
Food Distribution Optimization
## Project Overview
This topic is important because optimizing the distribution system from farms to tables in need will help lessen communities who struggle with hunger and limit overall waste, effectively increasing food efficiency.
Project Questions: Key questions include the following;
  1. Which areas within the United States suffer the highest food scarcity and/or food waste? (This can include restaurants and grocery chains, as well as communities, charities, and counties.)
  2. What is the most efficient way to transport excess from high waste areas to communities and charities with high food insecurity? (This can include routes or types of energy/vehicles.)
  3. How would these changes impact local, state, and federal economies and surrounding environments (in the sense that the benefits of redistribution outweigh the environmental/cost of drawbacks)?
Answers to these questions would first be maps of hot spots where there is high food insecurity, as well as maps showcasing areas of high food waste, preferably outlined as counties in various shades of a color depending on how bad the area either needs food or needs redistribution. The map would show restaurants, grocery chains, food banks, or communities that fit the above description, and main/cross country or cross county/state roads would also be labeled to show the best route to optimize food redistribution. AI could generate best routes, or a network map could be utilized to showcase this. There could also be supply and demand graphs for the main areas, as decided based on these maps, where a list of the most benefiting providers and receivers could be focused on for redistribution. As for the final question, line graphs (or bar graphs) could showcase carbon emissions from the use of transportation to redistribute food throughout the country to show the environmental impact, and a metric of cost savings from the theoretical cost of having this food waste go to landfills (where it instead is transported to other communities and food banks) would show the economic impact.

Data Sources: Much of the data would have to come from the USDA or food-related nonprofits, since those are the organizations who conduct this kind of research. 
  1. The USDA has a food access map chart that shows how food is scattered across the country, and this will show the areas with higher food insecurity to work with. It's an interactive map that can be used to pinpoint and then rank areas of high food insecurity and waste for redistribution.
  2. The EPA provides data for methods ranking the limitation of food waste, and this includes the impact of taking food away from landfills as files. In addition, ReFED has an insights engine that contains an impact calculator to download theoretical database data. This will provide information on the benefits and costs of redistributing food from landfills to food banks.
  3. The USDA also provides an agricultural marketing service that tracks the movement of food products through its supply chain journey. This data can be downloaded as datasets, showing truck rates and availability as volumes and as a use index. This will show routes and emissions produced by current methods and where exactly production is going.
## Self Assessment and Reflection

<!-- Edit the following section with your self assessment and reflection -->

### Self Assessment
<!-- Replace the (...) with your score -->

| Category          | Score    |
| ----------------- | -------- |
| **Setup**         | ... / 10 |
| **Execution**     | ... / 20 |
| **Documentation** | ... / 10 |
| **Presentation**  | ... / 30 |
| **Total**         | ... / 70 |

### Reflection
<!-- Edit the following section with your reflection -->

#### What went well?
#### What did not go well?
#### What did you learn?
#### What would you do differently next time?

---

## Getting Started
### Installing Dependencies

To ensure that you have all the dependencies installed, and that we can have a reproducible environment, we will be using `pipenv` to manage our dependencies. `pipenv` is a tool that allows us to create a virtual environment for our project, and install all the dependencies we need for our project. This ensures that we can have a reproducible environment, and that we can all run the same code.

```bash
pipenv install
```

This sets up a virtual environment for our project, and installs the following dependencies:

- `ipykernel`
- `jupyter`
- `notebook`
- `black`
  Throughout your analysis and development, you will need to install additional packages. You can can install any package you need using `pipenv install <package-name>`. For example, if you need to install `numpy`, you can do so by running:

```bash
pipenv install numpy
```

This will update update the `Pipfile` and `Pipfile.lock` files, and install the package in your virtual environment.

## Helpful Resources:
* [Markdown Syntax Cheatsheet](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Dataset options](https://it4063c.github.io/guides/datasets)