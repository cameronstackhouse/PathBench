from algorithms.configuration.configuration import Configuration
from simulator.services.services import Services
from structures import Size
from generator.generator import Generator
from simulator.services.resources.atlas import Atlas

# Initialize the configuration
config = Configuration()
config.generator = True
config.generator_nr_of_examples = 10  # Number of maps to generate
config.generator_gen_type = "uniform_random_fill"  # Type of map generation
config.generator_obstacle_fill_min = 0.1  # Minimum obstacle fill rate
config.generator_obstacle_fill_max = 0.3  # Maximum obstacle fill rate
config.generator_min_room_size = 50  # Minimum room size (for house type generation)
config.generator_max_room_size = 100  # Maximum room size (for house type generation)
config.num_dim = 2  # Number of dimensions (2 for 2D maps)
config.generator_size = 1000  # Size of the maps to generate

# Initialize the services
services = Services(config)

# Create a generator instance
generator = Generator(services)

# Define the parameters for the map generation
nr_of_samples = config.generator_nr_of_examples
dimensions = Size(config.generator_size, config.generator_size)
gen_type = config.generator_gen_type
fill_range = [config.generator_obstacle_fill_min, config.generator_obstacle_fill_max]
nr_of_obstacle_range = [100, 500]  # Example range for number of obstacles
min_map_range = [config.generator_min_room_size, config.generator_min_room_size + 1]
max_map_range = [config.generator_max_room_size, config.generator_max_room_size + 1]

# Generate maps and save them in JSON format
maps = generator.generate_maps(
    nr_of_samples=nr_of_samples,
    dimensions=dimensions,
    gen_type=gen_type,
    fill_range=fill_range,
    nr_of_obstacle_range=nr_of_obstacle_range,
    min_map_range=min_map_range,
    max_map_range=max_map_range,
    num_dim=config.num_dim,
    json_save=True  # Enable JSON saving
)
