//
//  MainResultsPage.swift
//  AlphaHacks
//
//  Created by Arpan Dhatt on 6/12/21.
//

import SwiftUI

struct MainResultsPage: View {
    @EnvironmentObject var appState: AppState
    
    var body: some View {
        VStack {
            Text("These are companies identified on the receipt. Select one of them to see additional details about their practices and available alternatives.")
            List(appState.companies, id: \.hashValue) { name in
                NavigationLink(
                    destination: CompanyDetailsView(company: "Test Company"),
                    label: {
                        Text(name)
                    })
            }.listStyle(InsetGroupedListStyle()).navigationTitle("Results")
        }
        
    }
}

struct MainResultsPage_Previews: PreviewProvider {
    static var previews: some View {
        NavigationView {
            MainResultsPage().environmentObject(AppState())
        }
    }
}
