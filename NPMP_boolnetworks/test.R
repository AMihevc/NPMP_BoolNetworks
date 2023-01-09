library(BoolNet)
represirator <- loadNetwork("represirator.txt")
#možna začetna stanja
zac_stanja1 <- list(0,0,0)
zac_stanja2 <- list(1,1,1)
zac_stanja3 <- list(0,0,1)
zac_stanja4 <- list(0,1,0)
zac_stanja5 <- list(0,1,1)
zac_stanja6 <- list(1,0,0)
zac_stanja7 <- list(1,0,1)
zac_stanja8 <- list(1,1,0)

#analiza poti do atraktorjev 
potDoAtraktorjev <- getPathToAttractor(represirator, zac_stanja)
potDoAtraktorjev

# Matkov simulacija simulira in izpiše nekko statisiko
simulacijaMarkov <- markovSimulation(represirator, 100, zac_stanja1, 0.001, TRUE)
simulacijaMarkov

# time table of a network: generira 8 random zacetnih stanj in jih simulira za 6 korakov 
# nevem čist kaj je ta synchronous 
casovnaTabela <- generateTimeSeries(represirator, 8, 6,'synchronous')
casovnaTabela

# poenostavi omrežje nevem če bo delal k je že tok simpl 
poenostavljeno <- simplifyNetwork(represirator)
poenostavljeno

# symbolic simulaicja ta nš i guess da ni symbolic tko da to ne dela
# sim <- simulateSymbolicModel(represirator)
# plotAttractors(sim)

# nek perturbe neki izpiše idk man 
perturbedNet1 <- perturbNetwork(represirator, perturb="functions", method="shuffle")
print(getAttractors(perturbedNet1))

