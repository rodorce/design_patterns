from patterns.Report import Report

class WebReport(Report):
    def create_content(self):
        builder = [self._create_headers(), self._create_table_headers()]
        for ride in self.rides:
            builder.append(self._add_ride(ride))
        builder.append(self._close_table_headers())

        return "".join(builder)
    
    def create_file(self, content:str):
        with open("financial-report-web.html", "w") as file:
            file.write(content)

    def _create_headers(self):
        return f"<h1>{self.headerTitle}</h1>"
    
    def _create_table_headers(self):
        return """
        <table>
            <tr>
                <th> TaxiID </th>
                <th> Pickup time </th>
                <th> Dropoff time </th>
                <th> Passenger count </th>
                <th> Trip Distance </th>
                <th> Total amount </th>
            </tr>
        """
    def _close_table_headers(self):
        return "</table>"

    def _add_ride(self, ride):
        return "".join([
            "<tr>",
            f"<td>{ride.taxi_id}</td>",
            f"<td>{ride.pick_up_time.isoformat()}</td>",
            f"<td>{ride.drop_of_time.isoformat()}</td>",
            f"<td>{ride.passenger_count}</td>",
            f"<td>{ride.trip_distance}</td>",
            f"<td>{self._format_amount(ride.tolls_amount)}</td>",
            "</tr>"
        ])
    
    def _format_amount(self, amount):
        if amount < 0:
            return f"<span style='color:red'>{amount}</span>"
        return str(amount)