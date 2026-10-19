import math


class ArogyaGridEngine:

  def __init__(self):
    # Simulated emergency medical inventory across regional hubs
    self.hubs = {
        'Hub_A': {'lat': 12.9716, 'lon': 77.5946, 'oxygen_cylinders': 45},
        'Hub_B': {'lat': 13.0827, 'lon': 80.2707, 'oxygen_cylinders': 120},
        'Hub_C': {'lat': 11.0168, 'lon': 76.9558, 'oxygen_cylinders': 15},
    }

  def calculate_distance(self, lat1, lon1, lat2, lon2):
    """Calculates Euclidean distance between two geographic points."""
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

  def find_optimal_supply_hub(
      self, hospital_lat, hospital_lon, required_units
  ):
    """Finds the nearest hub with sufficient inventory for immediate dispatch."""
    best_hub = None
    min_distance = float('inf')

    for hub_id, data in self.hubs.items():
      if data['oxygen_cylinders'] >= required_units:
        dist = self.calculate_distance(
            hospital_lat, hospital_lon, data['lat'], data['lon']
        )
        if dist < min_distance:
          min_distance = dist
          best_hub = hub_id

    return best_hub, min_distance


if __name__ == '__main__':
  engine = ArogyaGridEngine()

  # Emergency Request Simulation: Hospital needs 30 oxygen units
  hospital_coords = (11.0000, 76.9000)
  needed_units = 30

  allocated_hub, distance = engine.find_optimal_supply_hub(
      hospital_coords[0], hospital_coords[1], needed_units
  )

  print('=' * 50)
  print('       HEALTHMAP PREDICTIVE DISPATCH ENGINE       ')
  print('=' * 50)
  print(f'Incoming Emergency Demand: {needed_units} Units')
  print(f'Optimal Dispatch Hub: {allocated_hub}')
  print(f'Calculated Logistics Distance: {distance:.4f} units')
  print('Status: Dispatch Order Created Successfully.')
  print('=' * 50)
