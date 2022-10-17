from patterns.Report import Report


class PrintReport(Report):
    def create_content(self):
        builder = [self._create_headers(), self._create_table_headers()]
        for ride in self.rides:
            builder.append(self._add_ride(ride))
        return "".join(builder)
    
    def create_file(self, content:str):
        with open("financial-report-print.txt", "w") as file:
            file.write(content)

    def _create_headers(self):
        return f"{self.headerTitle}\n\n"
    
    def _create_table_headers(self):
        return "TaxiID \tPickup Time \tDropoff Time \tPassenger count \tTrip Distance \tTotal Amount \t"

    def _add_ride(self, ride):
        return "".join([
            f"\t{ride.taxi_id}",
            f"\t{ride.pick_up_time.isoformat()}",
            f"\t{ride.drop_of_time.isoformat()}",
            f"\t{ride.passenger_count}",
            f"\t{ride.trip_distance}",
            f"\t{self._format_amount(ride.tolls_amount)}",
        ])
    
    def _format_amount(self, amount):
        if amount < 0:
            return f"({amount})"
        return str(amount)