# Was It the Player or the Team?

Building a Bayesian skill model for soccer, live in PyMC. A 90-minute workshop at the
[Carnegie Mellon Sports Analytics Conference](https://www.stat.cmu.edu/cmsac/conference/), October 2026.

**[▶ Open the notebook in Colab](https://colab.research.google.com/github/AlexAndorra/cmsac-2026/blob/main/player_or_team.ipynb)**: nothing to install.

## What's here

| Path | What it is |
|---|---|
| `player_or_team.ipynb` | The session: a first Bayesian model, a hierarchical model of player skill, Gaussian processes for form and career stage, team factors, and out-of-sample validation |
| `data/` | Player-match data from the Soccer Factor Model; codebook in `data/README.md` |
| `tests/` | Runs the notebook end to end |

## Run locally

```bash
uv sync
uv run jupyter lab player_or_team.ipynb
uv run pytest  # executes the whole notebook, a few minutes
```

The model graphs need the [Graphviz](https://graphviz.org/download/) binary (`brew install graphviz` or `apt install graphviz`); Colab has it.

## Credits

The models come from the Soccer Factor Model: Andorra & Göbel (2024), *Unveiling True Talent: The Soccer Factor
Model for Skill Evaluation*, [arXiv:2412.05911](https://arxiv.org/abs/2412.05911). Live platform:
[soccerfactormodel.com](https://www.soccerfactormodel.com).
