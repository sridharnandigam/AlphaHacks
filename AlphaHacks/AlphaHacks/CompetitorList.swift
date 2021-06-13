//
//  CompetitorList.swift
//  AlphaHacks
//
//  Created by Arpan Dhatt on 6/12/21.
//

import SwiftUI

struct CompetitorList: View {
    @EnvironmentObject var appState: AppState
    var this_company: String
    
    var body: some View {
        List(appState.competitors, id: \.hashValue) {name in
            Text(name)
        }.listStyle(InsetGroupedListStyle()).navigationTitle(this_company)
    }
}

struct CompetitorList_Previews: PreviewProvider {
    static var previews: some View {
        NavigationView {
            CompetitorList(this_company: "Hi").environmentObject(AppState())
        }
    }
}
