import React, {useState} from 'react';
import { pokemonList } from './pokemonList';
import './App.css';

// Use npm start to start the server

function App() {
  const [count, setCount] = useState(0);
  const [selectedPokemon, setSelectedPokemon] = useState(pokemonList[0]);

  const handleIncrement = () => setCount(count + 1);
  const handleDecrement = () => setCount(count > 0 ? count - 1 : 0);
  const handleReset = () => setCount(0);
  return (
    <div className="App">
      <h1>Pokemon Counter App</h1>
            <select
        value={selectedPokemon.id}
        onChange={(e) => {
          const selected = pokemonList.find(
            (p) => p.id === parseInt(e.target.value)
          );
          setSelectedPokemon(selected);
          setCount(0); // Reset count when Pokémon changes
        }}
      >
        {pokemonList.map((pokemon) => (
          <option key={pokemon.id} value={pokemon.id}>
            {pokemon.name.charAt(0).toUpperCase() + pokemon.name.slice(1)}
          </option>
        ))}
      </select>
      <h2>{selectedPokemon.name.charAt(0).toUpperCase() +
          selectedPokemon.name.slice(1)}</h2>
      <img
        src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/shiny/${selectedPokemon.id}.png`}
        alt={selectedPokemon.name}
        style={{ width: "150px" }}
      />
      <h2>{count}</h2>
      <button class="Increment" onClick={handleIncrement}>+</button>
      <button class="Decrement"onClick={handleDecrement}>-</button>
      <button class="Reset"onClick={handleReset}>Reset</button>
    </div>
  );
}

export default App;
