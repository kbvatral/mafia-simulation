# Mafia Simulation
A simulation and game theoretic analysis of the common party game Mafia.
This research was developed as a final project for MA499 Game Theory at Eastern Nazarene College.

## Getting Started

The project is broken down into two parts: a game theoretic analysis and a python simulation to support the analysis.
The simulation can be found  under the `src/` folder and was written using Python 3 and the Anaconda distribution.
A PDF and latex source file for the analysis can be found under the `docs/` folder. 
The analysis also contains charts to summarize the results of the simulations.

## Running the Simulation

The easiest way to view the results from the simulation is to look at the game theoretic analysis PDF contained in the `docs/` folder. It uses results from all the simulation to support the analysis. However, each simulation can be run individually as well.

The simulation is written in Python 3 using the Anaconda distribution. 
It is possible to run the simulation using another distribution of Python, but several packages will have to be installed.
To run it, clone the repository and in the source folder, navigate to the simulation desired and run it with python. For example:

```bash
cd src/simple
python3 allValues.py
```

Depending on the simulation run, different kinds of charts will be outputted.

## Built With

* [Anaconda](https://anaconda.org) - The python distribution used int he simulations
* [MikTex](https://miktex.org/) - The latex compiler used for the analysis report

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Authors

* The analysis and all supporting code was developed by [**Caleb Vatral**](https://github.com/kbvatral)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Special thanks to Dr. Marcus Fries who guided me during the initial phases of this research

